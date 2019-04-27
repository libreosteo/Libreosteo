# This file is part of Libreosteo.
#
# Libreosteo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Libreosteo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Libreosteo.  If not, see <http://www.gnu.org/licenses/>.
from libreosteoweb import models
from libreosteoweb.api.utils import _unicode, convert_to_long
from datetime import datetime

class Generator(object):
    def __init__(self, office_settings, therapeut_settings):
        self.office_settings = office_settings
        self.therapeut_settings = therapeut_settings

    def generate_invoice(self, examination, serializer_data, request):
        invoice = models.Invoice()
        invoice.amount = serializer_data['amount']
        invoice.currency = self.office_settings.currency
        invoice.header = self.office_settings.invoice_office_header
        invoice.office_address_street = self.office_settings.office_address_street
        invoice.office_address_complement = self.office_settings.office_address_complement
        invoice.office_address_zipcode = self.office_settings.office_address_zipcode
        invoice.office_address_city = self.office_settings.office_address_city
        invoice.office_phone = self.office_settings.office_phone
        invoice.office_siret = self.office_settings.office_siret

        # Override the siret on the invoice with the therapeut siret if defined
        if self.therapeut_settings.siret is not None :
            invoice.office_siret = self.therapeut_settings.siret

        invoice.paiment_mode = serializer_data['paiment_mode']
        invoice.therapeut_name = request.user.last_name
        invoice.therapeut_first_name = request.user.first_name
        invoice.therapeut_id = request.user.id
        invoice.quality = self.therapeut_settings.quality
        invoice.adeli = self.therapeut_settings.adeli
        invoice.location = self.office_settings.office_address_city
        invoice.number = ""

        invoice.patient_family_name = examination.patient.family_name
        invoice.patient_original_name = examination.patient.original_name
        invoice.patient_first_name = examination.patient.first_name
        invoice.patient_address_street = examination.patient.address_street
        invoice.patient_address_complement = examination.patient.address_complement
        invoice.patient_address_zipcode = examination.patient.address_zipcode
        invoice.patient_address_city = examination.patient.address_city
        invoice.content_invoice = self.office_settings.invoice_content
        invoice.footer = self.office_settings.invoice_footer

        # Override the footer on the invoice with the therapeut settings if defined
        if self.therapeut_settings.invoice_footer is not None :
            invoice.footer = self.therapeut_settings.invoice_footer
        if self.office_settings.invoice_start_sequence is not None and len(self.office_settings.invoice_start_sequence) > 0:
            invoice.number = _unicode(convert_to_long(self.office_settings.invoice_start_sequence))
            self.office_settings.invoice_start_sequence = _unicode(convert_to_long(invoice.number) + 1)
        else :
            invoice.number = _unicode(10000)
            self.office_settings.invoice_start_sequence = _unicode(convert_to_long(invoice.number) + 1)
        invoice.date = datetime.today()
        return invoice

       
   
