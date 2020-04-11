def car_description(manufacturer,  model, **car_info):
  car_info['manufacturer'] = manufacturer
  car_info['model'] = model
  return car_info

subaru_car = car_description('Subaru', 'Impreza', color="red", engine='WRX')
print(subaru_car)