from django.contrib import admin


from .models import Instrument

class InstrumentList(admin.ModelAdmin):
    list_display = ['instrument_name' , 'status' , 'instrument_type' , 'location_type' , 'address', 'sample_quantity', 'booking_amount', 'operator', 'remarks',  'update' , 'image']
    list_filter = ['status', 'location_type', 'instrument_type']

admin.site.register(Instrument, InstrumentList)