# Forest Fire Detection

This project explores three distinct approaches for detecting forest fires using various image processing methods. Since the primary goal is object detection, classification techniques were not considered.

## Approach 1: YOLOv11

A pre-trained YOLOv11 network was fine-tuned for this task using annotated data prepared with Roboflow. Fine-tuning a pre-trained network proved to be more efficient and effective than employing complex image processing techniques.

## Approach 2: Image Processing

Different image processing methods were explored to assess the feasibility of detecting fire:

- **IR Imaging:** Fire and smoke clumps could be detected using binarization and thresholding. However, these methods required frequent adjustments for variations in video input, making them unsuitable for diverse images or sources.
- **Morphological Operations:** Morphological closing was applied to identify clumps resembling smoke and fire. Subsequently, Gaussian blur and Canny edge detection were used. While this approach yielded better results, it was still insufficient for robust detection.

## Approach 3: Feature Extraction

Feature extraction techniques were tested using OpenCV's ORB feature extractor and BFMatcher:

- This method demonstrated the potential to detect certain flame features in images.
- However, it struggled with inconsistent matches due to the varying colors and patterns of flames.
- Although this approach could be meaningful with a large dataset of diverse fire features, it is not reliable as a standalone method.

---

Each approach offers unique insights into forest fire detection, but further advancements are necessary to achieve a dependable solution across varying conditions.

