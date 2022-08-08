from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse
from .models import Video
from .services import open_file


def index(request):
    return render(
        request, 'index.html'
    )

def get_list_video(request):
    return render(request, 'list_video.html', {'video_list':Video.objects.all()})

def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "video.html", {"video": _video})

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
