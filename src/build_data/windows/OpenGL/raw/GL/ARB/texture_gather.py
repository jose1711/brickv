'''OpenGL extension ARB.texture_gather

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_gather'
_DEPRECATED = False
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = constant.Constant( 'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET', 0x8E5E )
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = constant.Constant( 'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET', 0x8E5F )
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS = constant.Constant( 'GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS', 0x8F9F )


def glInitTextureGatherARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
