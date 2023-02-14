import zeep
from zeep import xsd
# 4210201242284

client = zeep.Client(wsdl='https://api.mediaexpert.pl/?q=ws/wsdl/products', service_name='TergProductsDataService')
client2 = zeep.Client(wsdl='https://api.mediaexpert.pl/?q=ws/wsdl/products')
print(client2.service.testGet(http200=True))

print(client.service.prodsCMS2USPGet(prodID=xsd.SkipValue, prodIndex=xsd.SkipValue, prodEAN='4210201242284',
                                     insiderFlag=xsd.SkipValue, http200=False))
