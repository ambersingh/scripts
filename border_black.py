'''
For drawing a border to the image.
'''

from PIL import Image, ImageDraw


webhexcolor = ['#FF0000', '#00BFFF','#00FA9A', '#9932CC', '#6495ED', '#9370DB', '#800000', '#7B68EE', '#DAA520', '#C0C0C0', '#A52A2A', '#FA8072', '#FFC0CB', '#66CDAA', '#8FBC8F', '#FFDEAD', '#FFDAB9', '#808000', '#DEB887', '#FF4500', '#FFEBCD', '#6B8E23', '#2E8B57', '#008080', '#0000CD', '#FF1493', '#CD5C5C', '#CD853F', '#FFB6C1', '#F0E68C', '#ADFF2F', '#ADD8E6', '#E9967A', '#800080', '#696969', '#00CED1', '#008B8B', '#F08080', '#191970', '#F5DEB3', '#FFD700', '#FF6347', '#C71585', '#4B0082', '#BDB76B', '#FFA07A', '#00FFFF', '#98FB98', '#BC8F8F', '#00FF00', '#DDA0DD', '#FFFAFA', '#A0522D', '#D8BFD8', '#48D1CC', '#A9A9A9', '#708090', '#F0F8FF', '#FF00FF', '#2F4F4F', '#E0FFFF', '#1E90FF', '#556B2F', '#F4A460', '#228B22', '#8B008B', '#8B0000', '#FF7F50', '#87CEEB', '#32CD32', '#D3D3D3', '#006400', '#FFE4B5', '#FFFF00', '#AFEEEE', '#40E0D0', '#8A2BE2', '#20B2AA', '#DB7093', '#5F9EA0', '#00008B', '#808080', '#DC143C', '#D2B48C', '#D2691E', '#BA55D3', '#4682B4', '#4169E1', '#FAEBD7', '#000000', '#E6E6FA', '#FFE4E1', '#8B4513', '#FF8C00', '#B8860B', '#9ACD32', '#EEE8AA', '#7FFFD4', '#3CB371', '#B0C4DE', '#FFA500']

# Required dimension
dim = 9
thickness = 1.1

# Initial dimension
_dim = 720
_thickness = (_dim / dim) * thickness
for color in webhexcolor:
   img = Image.new("RGBA", (_dim, _dim))
   draw = ImageDraw.Draw(img)

   draw.ellipse((0, 0, _dim, _dim), fill='#2c2c2c')
   draw.ellipse((_thickness, _thickness, _dim -
                 _thickness, _dim - _thickness), fill=color)
   img = img.resize((dim, dim), Image.ANTIALIAS)
   img.save("circulars/" +
            color.split('#')[1] + ".png")