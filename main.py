import zeep
from zeep import xsd

client = zeep.Client(wsdl='https://api.mediaexpert.pl/?q=ws/wsdl/products', service_name='TergProductsDataService')
try:
    print(client.service.prodsCMS2USPGet(prodID=xsd.SkipValue, prodIndex=xsd.SkipValue, prodEAN='4210201242284',
                                         insiderFlag=xsd.SkipValue, http200=False))
except Exception as e:
    print(e)
