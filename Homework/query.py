from Models.service import Service
import mlab

mlab.connect()

id_to_find = "5af59fe0846ee81cc8b1e236"

# hera = Service.objects(id=id_to_find)
# hera = Service.objects.get(id=id_to_find)
hera = Service.objects.with_id(id_to_find)
if hera is not None:
    print(hera.address)
    # hera.delete()
    hera.update(set__address="Phố Vọng",set__height=173)
    hera.reload()
    print(hera.address)
    # print("Deleted")
else:
    print("Service not found")

# print(hera.to_mongo())

# all_service= Service.objects(gender=1)
#
# print(first_service['name'])
#
# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index == 9:
#         break
