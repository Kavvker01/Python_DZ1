from address import Address
from mailing import Mailing

address1 = Address("628417", "Сургут", "Ленина", "35", "27 кв")
address2 = Address("190022", "Санкт-Петербург", "Думская", "2/б", "24 кв")
track_num = ("190323139090")
cost_track = ("379")

mailing = Mailing(address1, address2, cost_track, track_num)

print(mailing)