from __future__ import unicode_literals

from django.conf import settings
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class SerializedObjectField(models.TextField):
    '''Model field that stores serialized value of model class instance
       and returns deserialized model instance

       >>> from django.db import models
       >>> import SerializedObjectField

       >>> class A(models.Model):
               object = SerializedObjectField(serialize_format='json')

       >>> class B(models.Model):
               field = models.CharField(max_length=10)
       >>> b = B(field='test')
       >>> b.save()
       >>> a = A()
       >>> a.object = b
       >>> a.save()
       >>> a = A.object.get(pk=1)
       >>> a.object
       <B: B object>
       >>> a.object.__dict__
       {'field': 'test', 'id': 1}

    '''

    def __init__(self, serialize_format='json', *args, **kwargs):
        self.serialize_format = serialize_format
        super(SerializedObjectField, self).__init__(*args, **kwargs)

    def db_type(self, connection=None):
        return 'text'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self._deserialize(value)

    def to_python(self, value):
        print("to_python")
        if isinstance(value, models.Model):
            print("models.Model")
            return value
        if value is None:
            return value
        return self._deserialize(value)

    def _serialize(self, value):
        if not value:
            return ''

        value_set = [value]
        if value._meta.parents:
            value_set += [getattr(value, f.name)
                          for f in list(value._meta.parents.values())
                          if f is not None]

        return serializers.serialize(self.serialize_format, value_set)

    def _deserialize(self, value):
        obj_generator = serializers.deserialize(
            self.serialize_format,
            value.encode(settings.DEFAULT_CHARSET),
            ignorenonexistent=True)

        obj = next(obj_generator).object
        for parent in obj_generator:
            for f in parent.object._meta.fields:
                try:
                    setattr(obj, f.name, getattr(parent.object, f.name))
                except ObjectDoesNotExist:
                    try:
                        # Try to set non-existant foreign key reference to None
                        setattr(obj, f.name, None)
                    except ValueError:
                        # Return None for changed_object if None not allowed
                        return None
        return obj

    def _serialize_if_object(self, value):
        if isinstance(value, str):
            # Check whether value can be deserialized
            self._deserialize(value)
            return value
        else:
            return self._serialize(value)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        return self._serialize_if_object(value)

    def get_prep_value(self, value):
        return self._serialize_if_object(value)
