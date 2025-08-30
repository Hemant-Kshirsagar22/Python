'''
Brand	            TEKCOOL                  ck_brand : str                
Color	            Grey White               ck_color : str
Display Type	    Digital                  ck_display_type : str
Style               Classic                  ck_style : str
Product Dimensions	32W x 5H Centimeters     ck_product_dimensions : dict
Power Source	    Battery Powered          ck_power_source : str
Shape               Round                    ck_shape : str
Usage	            Indoor                   ck_usage : str
Material	        Plastic                  ck_material : str
Frame Material	    Plastic                  ck_frame_material : str
'''

class Clock :
    def __init__(self,
                ck_brand : str,
                ck_color : str,
                ck_display_type : str,
                ck_style : str,
                ck_product_dimensions : dict,
                ck_power_source : str,
                ck_shape : str,
                ck_usage : str,
                ck_material : str,
                ck_frame_material : str
            ) :
        self.ck_brand = ck_brand
        self.ck_color = ck_color
        self.ck_display_type = ck_display_type
        self.ck_style = ck_style
        self.ck_product_dimensions = ck_product_dimensions 
        self.ck_power_source = ck_power_source
        self.ck_shape = ck_shape
        self.ck_usage = ck_usage
        self.ck_material = ck_material
        self.ck_frame_material = ck_frame_material

    def show(self) -> None :
        print(self.__dict__)
        
    def __str__(self) :
        return f'{self.__dict__}'

wall_clack = Clock(
    'TEKCOOL',
    'Grey White',
    'Digital',
    'Classic',
    {'W' : '32', 'H' : '5', 'UNIT' : 'CM'},
    'Battery Powered',
    'Round',
    'Indoor',
    'Plastic',
    'Plastic',
)

print(wall_clack)
wall_clack.show()