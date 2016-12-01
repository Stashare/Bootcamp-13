 if len(args) >= 3:
        self.car_type = args[2]
      else:
        self.car_type = 'saloon'
        
      if self.car_type == 'trailer':
        self.num_of_wheels = 8
      else:
       self.num_of_wheels = 4
       
      self.speed = 0
       
    def is_saloon(self):
      return self.car_type == 'saloon'
      
    def drive(self, spd):
      if self.car_type == 'trailer':
        self.speed = spd * 11
      else:
        self.speed = 10 ** spd
        
      return self
