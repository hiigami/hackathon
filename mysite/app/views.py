from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from moneyed import *

globar_harcodeado = {
    "accountant" : {
        "price": Money(amount="120.00", currency='MXN'),
        "info": "",
        "photo": ""
    }
}

class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Contratar(View):
    template_name = 'app/contratar.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

factura = """
<?xml version='1.0' encoding='UTF-8'?>
<cfdi:Comprobante xmlns:cfdi='http://www.sat.gob.mx/cfd/3' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:implocal='http://www.sat.gob.mx/implocal' xmlns:notariospublicos='http://www.sat.gob.mx/notariospublicos' xmlns:donat='http://www.sat.gob.mx/donat' xmlns:divisas='http://www.sat.gob.mx/divisas' xmlns:leyendasFisc='http://www.sat.gob.mx/leyendasFiscales' xmlns:pagoenespecie='http://www.sat.gob.mx/pagoenespecie' xmlns:valesdedespensa='http://www.sat.gob.mx/valesdedespensa' xsi:schemaLocation='http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd http://www.sat.gob.mx/implocal http://www.sat.gob.mx/sitio_internet/cfd/implocal/implocal.xsd http://www.sat.gob.mx/notariospublicos http://www.sat.gob.mx/sitio_internet/cfd/notariospublicos/notariospublicos.xsd http://www.sat.gob.mx/donat http://www.sat.gob.mx/sitio_internet/cfd/donat/donat11.xsd http://www.sat.gob.mx/divisas http://www.sat.gob.mx/sitio_internet/cfd/divisas/divisas.xsd http://www.sat.gob.mx/leyendasFiscales http://www.sat.gob.mx/sitio_internet/cfd/leyendasFiscales/leyendasFisc.xsd http://www.sat.gob.mx/pagoenespecie http://www.sat.gob.mx/sitio_internet/cfd/pagoenespecie/pagoenespecie.xsd http://www.sat.gob.mx/valesdedespensa http://www.sat.gob.mx/sitio_internet/cfd/valesdedespensa/valesdedespensa.xsd' version='3.2' serie='A' folio='891' fecha='{date}T12:08:43' sello='HFSN2FWVPOjB6TGgZiT2HKGENRVvhEUmI1CT6Fway9NR+MHl0WLTaDO8q+yvjyhIjTtmgqpG+e8LJtNYDCXCzpWbLNOnS+M9BvzYVmVokgwz+iOumrssGTwQoq/WY1O7yizpcOeW7ChQ8FlLGiP+nK20yZpisJx6ARjUfNhMS1w=' formaDePago='Pago en una sola exhibición' noCertificado='00001000000301362226' certificado='MIIEcjCCA1qgAwIBAgIUMDAwMDEwMDAwMDAzMDEzNjIyMjYwDQYJKoZIhvcNAQEFBQAwggGKMTgwNgYDVQQDDC9BLkMuIGRlbCBTZXJ2aWNpbyBkZSBBZG1pbmlzdHJhY2nDs24gVHJpYnV0YXJpYTEvMC0GA1UECgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNVBAsML0FkbWluaXN0cmFjacOzbiBkZSSTZWd1cmlkYWQgZJUgbGEgSW5mb3JtYWNpw7NuMR8wHQYJKoZIhvcNAQkBFhBhY29kc0BzYXQuZ29iLm14MSYwJAYDVQQJDB1Bdi4gSGlkYWxnbyA3NywgQ29sLiBHdWVycmVybzEOMAwGA1UEEQwFMDYzMDAxCzAJBgNVBAYTAk1YMRkwFwYDVQQIDBBEaXN0cml0byBGZWRlcmFsMRQwEgYDVQQHDAtDdWF1aHTDqW1vYzEVMBMGA1UELRMMU0FUOTcwNzAxTk4zMTUwMwYJKoZIhvcNAQkCDCZSZXNwb25zYWJsZTogQ2xhdWRpYSBDb3ZhcnJ1YmlhcyBPY1hvYTAeFw0xMzExMjExNjM0MDdaFw0xNzExMjExNjM0MDdaMIG+MSYwJAYDVQQDFB1FUklLQSBMRVRJQ0lBIEZFUk5BTkRFWiBNVdFPWjEmMCQGA1UEKRQdRVJJS0EgTEVUSUNJQSBGRVJOQU5ERVogTVXRT1oxJjAkBgNVBAoUHUVSSUtBIExFVElDSUEgRkVSTkFOREVaIE1V0U9aMRYwFAYDVQQtEw1GRU1FNzUwODIxNFNBMRswGQYDVQQFExJGRU1FNzUwODIxTURGUlhSMDMxDzANBgNVBAsTBlVOSURBRDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAg49NLRKCncZrRWgiGJDFv1863zvlYJWgUx92g4uvmKEuFhSDmuqr786ge5XPIKa3NJ9bn1BOboXoOD6ZDaGYbXr0WpTiqR0CAjK48/mk2se4Q9MiPyG71DjuLwcvUMrxru+sef5xrAZmu9dn+ALu9jRFK/clpr5bDvGMju/4sTMCAwEAAaMdMBswDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCBsAwDQYJKoZIhvcNAQEFBQADggEBALceQt8Puj6YOKQYxTC2pqtt2Ka4V32K3XWyjib/Ec/ibiZi4xk8G1abeGurAtQu424iQBVugsKxUMy0+aTI4KOx2iJ33lTQ9PQFtrsqWmfvSYE/NItJ0b08+elIa4mYTqswlEXqj/3ICJ1qN5VRiJXcx3Q9dSEFGg0OzW1rvyDs/DT2fKourCPrOKb8WJdQjYFyikhPoBCLinbkXAKaSPR/BxD60PL5k/h+e45dAoVNpUSrv2AUlQio3nhyZqC7DEzUfda5mblXDgnjsyUUaV0CEUoJjAswT84TcwhImqtJwCykA7TapHpDX00g5TnOHl7ZLeYhnQmCfP+G4GcGs58=' subTotal='{sum}' TipoCambio='1.00' Moneda='PESOS' total='{sum}' tipoDeComprobante='ingreso' metodoDePago='Tarjeta' LugarExpedicion='Benito Juárez, Distrito Federal'><cfdi:Emisor rfc='ERD7508214SA' nombre='LUCA LUCRECIA FERNANDEZ MUÑOZ'><cfdi:DomicilioFiscal calle='Insurgentes Sur' noExterior='1024' noInterior='51' colonia='Crédito Constructor' municipio='Benito Juárez' estado='Distrito Federal' pais='México' codigoPostal='01940'/><cfdi:RegimenFiscal Regimen='Persona fisica con actividad empresarial y profesional'/></cfdi:Emisor><cfdi:Receptor rfc='POEN601219ZT1' nombre='{name}'><cfdi:Domicilio calle='AV. SAN TOLUCA' noExterior='71' noInterior='41' colonia='SAN TOLUCO' municipio='INSURGENTES' estado='D.F.' pais='MÉXICO' codigoPostal='11291'/></cfdi:Receptor><cfdi:Conceptos><cfdi:Concepto cantidad='1.00' unidad='PZ' descripcion='HONORARIOS MÉDICOS' valorUnitario='{sum}' importe='{sum}'/></cfdi:Conceptos><cfdi:Impuestos totalImpuestosTrasladados='0.00'><cfdi:Traslados><cfdi:Traslado impuesto='IVA' tasa='0.00' importe='0.00'/></cfdi:Traslados></cfdi:Impuestos><cfdi:Complemento><tfd:TimbreFiscalDigital version='1.0' UUID='1F9AC5FF-616C-4EB3-B6A9-6E3EBEDD9103' FechaTimbrado='{date}T12:09:32' selloCFD='HFSN2FWVPOjB6TGgZjT2HKGWNRVvhEUmI1CT6Fway9NR+MHl0WLTaDO8q+yvjyhIjTtmgqpG+e8LJlNYdCXCzpWaLNOnS+M9AvzYVmVokgwz+iZumrssGTwQoq/WY1O7yizpcOeW7ChQ8FlLGiP+nK20yZpisJx6ARjUfNhMS1w=' noCertificadoSAT='00001000000301031501' selloSAT='dVaLq76ef07AaoSTUsTZ+Gb86ZDp4jR2x1QhNMCbxkaHLtXL6nM0jQR4uTgXRJ+j5OdpF5ZNysp+TTprRlEiNNobAQlBvJIRdo3qNzggLDjmtyDfW7UTRXv10ZPccGMOMSEyG3TwvKejR75ZoDUpwpb1vhWlQEIa/I16yiekA1U=' xsi:schemaLocation='http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/TimbreFiscalDigital/TimbreFiscalDigital.xsd ' xmlns:tfd='http://www.sat.gob.mx/TimbreFiscalDigital' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'/></cfdi:Complemento></cfdi:Comprobante>
"""

class Dashboard(View):
    template_name = 'app/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"factura": factura})

class DashboardUser(View):
    template_name = 'app/dashboard2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)