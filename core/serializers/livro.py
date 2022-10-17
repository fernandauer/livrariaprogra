from rest_framework.serializers import ModelSerializer

from core.models import Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        # depth = 1

...
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from media.models import Image
from media.serializers import ImageSerializer
...
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)


class LivroDetailSerializer(ModelSerializer):

    capa = ImageSerializer(required=False)