from requests import request
from rest_framework import serializers

from .validators import validate_title
from .models import Product
from rest_framework.reverse import reverse




class ProductSerializer(serializers.ModelSerializer):
    # if we need to serilaize field in api and we don't have it in model
    detial_view = serializers.SerializerMethodField(read_only=True)

    # in this case i added a email field , then add it in field array
    # email=serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            "pk",
            "title",
            "detial_view",
            "content",
            "price",
            "sale_price",
        ]


    title=serializers.CharField(validators=[validate_title])

    """
    This method to show detail-view in api , 
    """
    def get_detial_view(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
