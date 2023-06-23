from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Notary, Rate, Page, PageContent


class NotarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Notary
        fields = [
            "id",
            "name",
            "account",
            "address",
            "house_number",
            "latitude",
            "longitude",
            "phone",
            "whatsapp",
            "telegram",
            "email",
            "website",
            "description",
            "image",
            "schedule"
        ]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "account": UserSerializer(instance.account).data,
            "address": instance.address,
            "house_number": instance.house_number,
            "latitude": instance.latitude,
            "longitude": instance.longitude,
            "phone": instance.phone,
            "whatsapp": instance.whatsapp,
            "telegram": instance.telegram,
            "email": instance.email,
            "website": instance.website,
            "description": instance.description,
            "image": instance.image.url if instance.image else None,
            "schedule": instance.schedule
        }


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = [
            "id",
            "notary",
            "user",
            "rate",
        ]
        read_only_fields = [
            "id",
            "user",
        ]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "notary": {
                "id": instance.notary.id,
                "name": instance.notary.name,

            },
            "rate": instance.rate,
            "user": UserSerializer(instance.user).data,
        }


class PageContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageContent
        fields = [
            "id",
            "page",
            "title",
            "content",
            "footer",
            "body",
            "class_name",
            "order",
            "style",
        ]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "page": {
                "id": instance.page.id,
                "name": instance.page.name,
                "slug": instance.page.slug,
            },
            "title": instance.title,
            "content": instance.content,
            "footer": instance.footer,
            "body": instance.body,
            "class_name": instance.class_name,
            "order": instance.order,
            "style": instance.style,
        }


class PageSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Page
        fields = [
            "id",
            "name",
            "slug",
            "contents",
        ]
        read_only_fields = [
            "id",
            "slug",
            "contents",
        ]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "slug": instance.slug,
            "contents": PageContentSerializer(instance.contents.all(), many=True).data
        }
