import torch
import cv2
from ai_42_vienna.vision.streamer import FrameStreamer

# https://medium.com/artificialis/getting-started-with-depth-estimation-using-midas-and-python-d0119bfe1159


def instantiate_model():
    """
    Instantiate the MiDaS model for depth estimation

    Args:
        None

    Returns:
        midas: MiDaS model for depth estimation
        transform: MiDaS transform
    """

    model_types = ["DPT_Large",
                   "DPT_Hybrid",
                   "MiDaS_small"]

    model = model_types[2]

    midas = torch.hub.load("intel-isl/MiDaS", model)

    device = torch.device("mps")
    midas.to(device)

    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

    if model == "DPT_Large" or model == "DPT_Hybrid":
        transform = midas_transforms.dpt_transform
    else:
        transform = midas_transforms.small_transform

    return midas, transform


def main():
    """
    Main function for depth estimation

    Args:
        None

    Returns:
        None
    """

    midas, transform = instantiate_model()

    streamer = FrameStreamer(source=0, object_detection_model=None,
                             pose_estimation_model=None, depth_estimation_model=midas)
    while True:
        ret, frame = streamer.read()
        if not ret:
            break
        processed_frame = streamer.depth_estimation(frame, transform)
        streamer.show_frame(processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
