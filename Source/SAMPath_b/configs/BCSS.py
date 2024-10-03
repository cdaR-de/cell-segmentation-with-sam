from box import Box

config = {
    "batch_size": 6,
    "accumulate_grad_batches": 2,
    "num_workers": 4,
    "out_dir": "/kaggle/working/results",
    #/kaggle/working/results
    #/data07/shared/jzhang/result/Concept/sam_trial/BCSS
    "opt": {
        "num_epochs": 32,
        "learning_rate": 1e-4,
        "weight_decay": 1e-2, #1e-2,
        "precision": 32, # "16-mixed"
        "steps":  [72 * 25, 72 * 29],
        "warmup_steps": 72,
    },
    "model": {
        "type": 'vit_b',
        "checkpoint": "/kaggle/working/sam/weights/sam_vit_b_01ec64.pth",
        "freeze": {
            "image_encoder": True,
            "prompt_encoder": True,
            "mask_decoder": False,
        },
        "prompt_dim": 256,
        "prompt_decoder": False,
        "dense_prompt_decoder": False,

        "extra_encoder": 'hipt',
        "extra_type": "fusion",
        "extra_checkpoint": "/kaggle/working/hipt/weights/vit256_small_dino.pth",
        #/kaggle/working/hipt/weights/vit256_small_dino.pth
        #/data07/shared/jzhang/result/weights/HIPT/vit256_small_dino.pth
    },
    "loss": {
        "focal_cof": 0.25,
        "dice_cof": 0.75,
        "ce_cof": 0.0,
        "iou_cof": 0.0625,
    },
    "dataset": {
        "dataset_root": "/kaggle/working/merged_dataset_bcss/bcss_or",
        "dataset_csv_path": "/kaggle/working/SAMPath_b/SAMPath_b/dataset_cfg/BCSS_cv.csv",
        "val_fold_id": 0,
        "num_classes": 6,

        "ignored_classes": (0),
        "ignored_classes_metric": None, # if we do not count background, set to 1 (bg class)
        "image_hw": (1024, 1024), # default is 1024, 1024

        "feature_input": False, # or "True" for *.pt features
        "dataset_mean": (0.485, 0.456, 0.406),
        "dataset_std": (0.229, 0.224, 0.225),
    }
}

cfg = Box(config)