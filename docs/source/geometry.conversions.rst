kornia.geometry.conversions
==================================

.. meta::
   :name: description
   :content: "The kornia.geometry.conversions module provides a collection of functions for converting between various geometric representations, such as angles, coordinates, homographies, quaternions, rotation matrices, and Euler angles. This module includes utilities for transforming points between homogeneous and non-homogeneous coordinates, normalizing and denormalizing pixel coordinates, as well as handling pose transformations and quaternion operations for 3D geometry tasks."

.. currentmodule:: kornia.geometry.conversions

Angles
------

.. autofunction:: rad2deg
.. autofunction:: deg2rad
.. autofunction:: pol2cart
.. autofunction:: cart2pol
.. autofunction:: angle_to_rotation_matrix

Coordinates
-----------

.. autofunction:: convert_points_from_homogeneous
.. autofunction:: convert_points_to_homogeneous
.. autofunction:: convert_affinematrix_to_homography
.. autofunction:: denormalize_pixel_coordinates
.. autofunction:: normalize_pixel_coordinates
.. autofunction:: denormalize_pixel_coordinates3d
.. autofunction:: normalize_pixel_coordinates3d
.. autofunction:: normalize_points_with_intrinsics
.. autofunction:: denormalize_points_with_intrinsics


Homography
----------

.. autofunction:: normalize_homography
.. autofunction:: denormalize_homography
.. autofunction:: normalize_homography3d

Quaternion
----------

.. autofunction:: quaternion_to_axis_angle
.. autofunction:: quaternion_to_rotation_matrix
.. autofunction:: quaternion_log_to_exp
.. autofunction:: quaternion_exp_to_log
.. autofunction:: normalize_quaternion

Vector
------

.. autofunction:: vector_to_skew_symmetric_matrix

Rotation Matrix
---------------

.. autofunction:: rotation_matrix_to_axis_angle
.. autofunction:: rotation_matrix_to_quaternion

Axis Angle
----------

.. autofunction:: axis_angle_to_quaternion
.. autofunction:: axis_angle_to_rotation_matrix

Euler Angles
------------

.. autofunction:: quaternion_from_euler
.. autofunction:: euler_from_quaternion

Pose
----------

.. autofunction:: Rt_to_matrix4x4
.. autofunction:: matrix4x4_to_Rt
.. autofunction:: worldtocam_to_camtoworld_Rt
.. autofunction:: camtoworld_to_worldtocam_Rt
.. autofunction:: camtoworld_graphics_to_vision_4x4
.. autofunction:: camtoworld_vision_to_graphics_4x4
.. autofunction:: camtoworld_graphics_to_vision_Rt
.. autofunction:: camtoworld_vision_to_graphics_Rt
.. autofunction:: ARKitQTVecs_to_ColmapQTVecs
