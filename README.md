# CS256-AI-ObjectDetection

## Summary
Our main objective is to improve human/object detection on low-light images. We've used [EnlightenGAN](https://github.com/TAMU-VITA/EnlightenGAN) and have also tried EnlightenGAN with different combinations of filters such as CLAHE-Contrast Limited Adaptive Histogram Equalization and USM-Unsharp Mask to enlighten low-light images. We have then used [FasterRCNN](https://github.com/facebookresearch/detectron2) for object detection on these enlightened images and found significant improvement in the performance.

## INSTALLATION
See [INSTALL_EnlightenGAN.md](https://github.com/ksheeraj/CS256-AI-ObjectDetection/blob/master/INSTALL_EnlightenGAN)

## Quickstart
See [GETTING_STARTED.md](https://github.com/ksheeraj/CS256-AI-ObjectDetection/blob/master/GETTING_STARTED.md), or the [Colab Notebook](https://colab.research.google.com/drive/1RaWxgclMB8RpITo8Kci1qTecfm8iT61z#scrollTo=dq9GY37ml1kr).

## Citing Detectron2 and EnlightenGAN

```@misc{wu2019detectron2,
  author =       {Yuxin Wu and Alexander Kirillov and Francisco Massa and
                  Wan-Yen Lo and Ross Girshick},
  title =        {Detectron2},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2019}
}

  @article{jiang2019enlightengan,
  title={EnlightenGAN: Deep Light Enhancement without Paired Supervision},
  author={Jiang, Yifan and Gong, Xinyu and Liu, Ding and Cheng, Yu and Fang, Chen and Shen, Xiaohui and Yang, Jianchao and Zhou, Pan and Wang, Zhangyang},
  journal={arXiv preprint arXiv:1906.06972},
  year={2019}
}
```
## About:

This page(code, report and presentation) is the Group A submission for the final project of the course CS256: Topics in Artificial Intelligence, Section 2 at San Jose State University. Led by Instructor: Mashhour Solh, Ph.D.

The group members are: Anket Sah, Amala Chirayil, Ksheeraj Sai Vepuri, Kriti Gupta, Sanmesh Bhosale.

The code maybe used for educational and commercial use under no warranties. For questions on this project and code please reach out to: amalachirayil@gmail.com.

Credits:

This project was conducted with free credits provided by AWS Educate Team. Thank you AWS!
