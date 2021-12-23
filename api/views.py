from django.conf import settings
from django.http import HttpRequest, HttpResponse


def melon_list(request: HttpRequest) -> HttpResponse:
    json_path = settings.BASE_DIR / "api" / "assets" / "melon_data.json"
    with json_path.open(encoding="utf8") as f:
        return HttpResponse(f.read(), content_type="application/json")
