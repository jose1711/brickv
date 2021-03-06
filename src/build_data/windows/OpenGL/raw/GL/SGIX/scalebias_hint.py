'''OpenGL extension SGIX.scalebias_hint

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_scalebias_hint'
_DEPRECATED = False
GL_SCALEBIAS_HINT_SGIX = constant.Constant( 'GL_SCALEBIAS_HINT_SGIX', 0x8322 )


def glInitScalebiasHintSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
