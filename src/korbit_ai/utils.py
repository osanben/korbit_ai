"""
Korbit AI 工具函数模块
"""

import json
import os
import pickle
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import numpy as np
import pandas as pd


def load_config(config_path: Union[str, Path]) -> Dict[str, Any]:
    """
    加载配置文件
    
    Args:
        config_path: 配置文件路径
        
    Returns:
        配置字典
    """
    config_path = Path(config_path)
    
    if config_path.suffix == '.json':
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported config format: {config_path.suffix}")


def save_config(config: Dict[str, Any], config_path: Union[str, Path]) -> None:
    """
    保存配置文件
    
    Args:
        config: 配置字典
        config_path: 配置文件路径
    """
    config_path = Path(config_path)
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def load_data(file_path: Union[str, Path]) -> Union[pd.DataFrame, np.ndarray, Any]:
    """
    加载数据文件
    
    Args:
        file_path: 数据文件路径
        
    Returns:
        加载的数据
    """
    file_path = Path(file_path)
    
    if file_path.suffix == '.csv':
        return pd.read_csv(file_path)
    elif file_path.suffix == '.json':
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif file_path.suffix == '.pkl':
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    elif file_path.suffix in ['.npy']:
        return np.load(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")


def save_data(data: Any, file_path: Union[str, Path]) -> None:
    """
    保存数据到文件
    
    Args:
        data: 要保存的数据
        file_path: 文件路径
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if file_path.suffix == '.csv' and isinstance(data, pd.DataFrame):
        data.to_csv(file_path, index=False)
    elif file_path.suffix == '.json':
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    elif file_path.suffix == '.pkl':
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
    elif file_path.suffix == '.npy' and isinstance(data, np.ndarray):
        np.save(file_path, data)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")


def create_directories(dirs: List[Union[str, Path]]) -> None:
    """
    创建目录
    
    Args:
        dirs: 目录列表
    """
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True) 