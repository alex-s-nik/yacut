from flask import flash, redirect, render_template

from yacut import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/')
def index_view():
    form = URLMapForm()

    if not form.validate_on_submit():
        return render_template('', form=form)
    
    short_link = form.custom_id.text

    if short_link:
        if db.session.query(db.exists().where(URLMap.short == short_link)).scalar():
            flash('Такая короткая ссылка уже есть в сервисе')
            return render_template('', form=form)
        else:
            new_link = URLMap(
                original = form.original_link.text,
                short = short_link
            )
            db.session.add(new_link)
            db.session.commit()
            return render_template('', form=form, generated_link=new_link)
    while True:
        short_link = get_unique_short_id()
        if not db.session.query(db.exists().where(URLMap.short == short_link)).scalar():
            new_link = URLMap(
                original = form.original_link.text,
                short = short_link
            )
            db.session.add(new_link)
            db.session.commit()
            return render_template('', form=form, generated_link=new_link)

@app.route('/<str:link_id>')
def redirect_view(link_id: str):
    original_link = URLMap.query.get_or_404(short=link_id)
    return redirect(original_link)
