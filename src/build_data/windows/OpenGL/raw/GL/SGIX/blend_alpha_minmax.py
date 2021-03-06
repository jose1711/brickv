'''OpenGL extension SGIX.blend_alpha_minmax

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_blend_alpha_minmax'
_DEPRECATED = False
GL_ALPHA_MIN_SGIX = constant.Constant( 'GL_ALPHA_MIN_SGIX', 0x8320 )
GL_ALPHA_MAX_SGIX = constant.Constant( 'GL_ALPHA_MAX_SGIX', 0x8321 )


def glInitBlendAlphaMinmaxSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
