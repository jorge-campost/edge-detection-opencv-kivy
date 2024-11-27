from dataclasses import dataclass, field


@dataclass
class Params:
    kernel_size: int = field(default=3)
    edge_detection_method: str = field(default="sobel")
