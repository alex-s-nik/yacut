from flask import flash, redirect, render_template, url_for

from yacut import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()

    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    short_link = form.custom_id.data

    if short_link:
        if db.session.query(db.exists().where(URLMap.short == short_link)).scalar():
            flash('Такая короткая ссылка уже есть в сервисе')
            return render_template('index.html', form=form)

        new_link = URLMap(
            original=form.original_link.data,
            short=short_link
        )
        db.session.add(new_link)
        db.session.commit()
        flash(url_for('redirect_view', link_id=new_link.short, _external=True))
        return render_template('index.html', form=form)

    while True:
        short_link = get_unique_short_id()
        if not db.session.query(db.exists().where(URLMap.short == short_link)).scalar():
            new_link = URLMap(
                original=form.original_link.data,
                short=short_link
            )
            db.session.add(new_link)
            db.session.commit()
            flash(url_for('redirect_view', link_id=new_link.short, _external=True))
            return render_template('index.html', form=form)


@app.route('/<string:link_id>')
def redirect_view(link_id: str):
    original_link = URLMap.query.filter_by(short=link_id).first_or_404().original
    return redirect(original_link)
