def get_layer_position(viewer, layer_name):
    for i, layer in enumerate(viewer.layers):
        if layer.name == layer_name:
            return i
    return None


def refine_labels(label_image, min_area=300):
    import pyclesperanto_prototype as cle
    import napari_simpleitk_image_processing as nsitk
    import numpy as np
    # from skimage.measure import label
    # Exclude background label
    label_image = np.where(label_image == 1, 0, 1)

    # Post-processing
    label_image_closed = cle.closing_labels(label_image, None, 1.0)
    label_image_filled = nsitk.binary_fill_holes(label_image_closed)
    # Instance segmentation
    labels_post_processed = cle.label(label_image_filled)
    labels_post_processed = cle.exclude_small_labels(labels_post_processed, None, min_area)

    return labels_post_processed
