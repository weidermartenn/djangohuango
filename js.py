class OldGPSDevice:
    def get_coordinates(self):
        return 0, 0



class CoordinateFormatter:
    def get_coordinates(self):
        raise NotImplementedError("Метод get_coordinates должен быть реализован.")



class GPSAdapter(CoordinateFormatter):
    def __init__(self, gps_device):
        self.gps_device = gps_device

    def get_coordinates(self):
        lat, lon = self.gps_device.get_coordinates()
        return f"{lat}, {lon}"  # Возвращает координаты в нужном формате
    



def main():
    # Создаем экземпляр старого GPS-устройства
    old_gps_device = OldGPSDevice()
    
    # Создаем адаптер для старого устройства
    gps_adapter = GPSAdapter(old_gps_device)
    
    # Используем адаптер для получения координат
    coordinates = gps_adapter.get_coordinates()
    print(f"Координаты: {coordinates}") 

if __name__ == "__main__":
    main()

