def get_layer_position(viewer, layer_name):
    """
    Get the position of a layer in the viewer by its name.
    
    Parameters:
    -----------
    viewer : napari.Viewer
        The napari viewer instance.
    layer_name : str
        The name of the layer to find.
    Returns:
    --------
    int or None
        The index of the layer if found, otherwise None.
    """
    for i, layer in enumerate(viewer.layers):
        if layer.name == layer_name:
            return i
    return None


def refine_labels(label_image, min_area=300):
    """
    Refine labels in a label image by closing, filling holes, and excluding small labels.

    Parameters:
    -----------
    label_image : numpy.ndarray
        The input label image to be refined.
    min_area : int, optional
        The minimum area for labels to be retained. Default is 300.

    Returns:
    --------
    numpy.ndarray
        The refined label image with post-processed labels.
    """
    import pyclesperanto_prototype as cle
    import napari_simpleitk_image_processing as nsitk
    import numpy as np
    # Exclude background label
    label_image = np.where(label_image == 1, 0, 1)

    # Post-processing
    label_image_closed = cle.closing_labels(label_image, None, 1.0)
    label_image_filled = nsitk.binary_fill_holes(label_image_closed)
    # Instance segmentation
    labels_post_processed = cle.label(label_image_filled)
    labels_post_processed = cle.exclude_small_labels(labels_post_processed, None, min_area)

    return labels_post_processed
