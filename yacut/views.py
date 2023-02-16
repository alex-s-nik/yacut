from flask import flash, redirect, render_template, url_for

from yacut import app
from .forms import URLMapForm
from .services import create_new_link, get_original_link_by_short, short_link_exists
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()

    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    short_link = form.custom_id.data

    if short_link:
        if short_link_exists(short_link):
            flash(f'Имя {short_link} уже занято!', 'is_used')
            return render_template('index.html', form=form)

        new_link = create_new_link(form.original_link.data, short_link)
        url = url_for('redirect_view', short_link_id=new_link.short, _external=True) 
        flash(url, 'url_ready')
        return render_template('index.html', form=form)

    short_link = get_unique_short_id()
    new_link = create_new_link(form.original_link.data, short_link)
    url = url_for('redirect_view', short_link_id=new_link.short, _external=True) 
    flash(url, 'url_ready')
    return render_template('index.html', form=form)


@app.route('/<string:short_link_id>')
def redirect_view(short_link_id):
    original_link = get_original_link_by_short(short_link_id)
    return redirect(original_link)
