from flask import render_template, flash, redirect, session, url_for, request, g
from .models import Song
from .forms import SongForm, EditForm, DeleteForm, SortForm
from app import app, db


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    #user = {'nickname': 'Miguel'}
    

    songs = Song.query.all()
    songs.reverse()

    return render_template('index.html',
                           title='Home',
                           #user=user,
                           songs=songs)

def find_largest_id():
    max_id_val= 0
    for song in Song.query.all():
        if song.id > max_id_val:
            max_id_val = song.id
    return max_id_val

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if len(Song.query.all()) > 0:
        id_val = find_largest_id() + 1
    else:
        id_val = 1
    form = SongForm()
    if form.validate_on_submit():
        song = Song(id = id_val,name=form.name.data, ragam=form.ragam.data,
            talam=form.talam.data, link=form.link.data,
            artist = form.artist.data)
        db.session.add(song)
        db.session.commit()
        flash(song.name + ' is now posted!')
        return redirect(url_for('index'))
    return render_template('add.html',
        title = 'Add Song', form =form)

#@app.route('/edit')
@app.route('/edit/<int:song_id>', methods=['GET','POST'])
def edit(song_id):
    try:
        song = db.session.query(Song).filter(Song.id == song_id).first()
        
        form = EditForm(obj=song)
        del_form = DeleteForm()
        if request.method == 'POST'  and form.validate_on_submit():
                form.populate_obj(song)
                db.session.commit()
                flash(song.name + ' has been sucessfully edited')
                return redirect(url_for('index'))
        
        if request.method == 'POST' and del_form.validate_on_submit():
            db.session.delete(song)
            db.session.commit()
            flash('Song has been sucessfully deleted')
            return redirect(url_for('index'))
        return render_template('edit.html', title = 'Edit Song' , del_form = del_form,form = form, SONG_ID = song_id)
    except Exception as e:
        return(str(e))

@app.route('/sorted_by', methods=['GET','POST'])
def sorted_by():
    try:
        form = SortForm()
        songs = Song.query.all()
        songs.reverse()
        if request.method == 'POST' and form.validate_on_submit():
            if (form.sort_choice.data == 'ragam') and len(Song.query.filter(Song.ragam.ilike("%"+form.sort_val.data+"%")).all()) > 0:
                songs = Song.query.filter(Song.ragam.ilike("%"+form.sort_val.data+"%")).all()
            elif (form.sort_choice.data == 'talam' and len(Song.query.filter(Song.talam.ilike("%"+form.sort_val.data+"%")).all())>0):
                songs = Song.query.filter(Song.talam.ilike("%"+form.sort_val.data+"%")).all()
            elif (form.sort_choice.data == 'artist' and len(Song.query.filter(Song.artist.ilike("%"+form.sort_val.data+"%")).all())>0):
                songs = Song.query.filter(Song.artist.ilike("%"+form.sort_val.data+"%")).all()
            elif (form.sort_choice.data == 'name' and len(Song.query.filter(Song.name.ilike("%"+form.sort_val.data+"%")).all())>0):
                songs = Song.query.filter(Song.name.ilike("%"+form.sort_val.data+"%")).all()
            elif (form.sort_choice.data == 'varanam' and len(Song.query.filter(Song.name.ilike("%varanam%") | Song.name.ilike('%varnam%')).all())>0):
                songs = Song.query.filter(Song.name.ilike("%varanam%") | Song.name.ilike('%varnam%')).all()
            else:
                #flash('sort fail')
                songs = Song.query.all()
            #flash(form.sort_choice.data + " and " + form.sort_val.data)
            return render_template('sorted_by.html',
                           title='Song Sorting',
                           form=form,
                           songs=songs)
        return render_template('sorted_by.html', title = 'Song Sorting', form =form, songs = songs)
    except Exception as e:
        return(str(e))
