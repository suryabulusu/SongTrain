from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#imported os to change directory
import os
from compare import freq_array
#from sound_record import record_user
from freq_plot import frequency_plot

#from uploads.core.models import Document
#from uploads.core.forms import DocumentForm


#def home(request):
#     documents = Document.objects.all()
#     return render(request, 'core/home.html', { 'documents': documents })
freq_karaoke = []
freq_recording = []
time = []
name_of_song = ' '
length = 0
def home(request):
    return render(request, 'core/home.html')
    
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        import separateLeadStereoParam
        new_name = 'media/' + filename
        separateLeadStereoParam.main(new_name)
        os.chdir('media/karaoke/')
        os.rename('estimated_music_VUIMM.wav',filename)
        global freq_karaoke
        global time
        global length
        freq_karaoke, time = freq_array(filename)
        length = len(time)
        print len(freq_karaoke)
        print len(time)
        #freq_karaoke = freq_karaoke[0:length-1]
        global name_of_song
        name_of_song = filename
        os.chdir('..')
        os.chdir('..')
        #print uploaded_file_url
        karaoke_url ='media/karaoke/' + filename

        return render(request, 'core/record.html', {
            'uploaded_file_url': uploaded_file_url, 'filename': filename,
            'karaoke_url': karaoke_url
        })

    return render(request, 'core/simple_upload.html')

def record_play(request):
   if request.method == 'POST' and request.FILES['myfile1']:
        myfile1 = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename1 = fs.save(myfile1.name, myfile1)
        uploaded_file1_url = fs.url(filename1)
        global freq_recording
        global time
        global length
        os.chdir('media/')
        freq_recording, time1 = freq_array(filename1)
        freq_recording1 = freq_recording[0:length]
        os.chdir('png/')
        print len(freq_recording1)
        print len(time)
        frequency_plot(time, freq_karaoke, freq_recording1)
        image_url = 'media/png/foo.png'
        os.chdir('..')
        os.chdir('..')
        return render(request, 'core/final.html',{'image_url':image_url})
   karaoke_url ='media/karaoke/' + name_of_song
   return render(request, 'core/evaluate.html', {'karaoke_url': karaoke_url})