"""
测试工具函数模块
"""

import json
import tempfile
import pytest
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# 添加src目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from korbit_ai.utils import load_config, save_config, load_data, save_data, create_directories


class TestUtils:
    """测试工具函数"""
    
    def test_save_and_load_config(self):
        """测试配置文件的保存和加载"""
        config = {"test": "value", "number": 123}
        
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "test_config.json"
            
            # 测试保存
            save_config(config, config_path)
            assert config_path.exists()
            
            # 测试加载
            loaded_config = load_config(config_path)
            assert loaded_config == config
    
    def test_save_and_load_csv_data(self):
        """测试CSV数据的保存和加载"""
        data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "test_data.csv"
            
            # 测试保存
            save_data(data, file_path)
            assert file_path.exists()
            
            # 测试加载
            loaded_data = load_data(file_path)
            pd.testing.assert_frame_equal(data, loaded_data)
    
    def test_save_and_load_json_data(self):
        """测试JSON数据的保存和加载"""
        data = {"test": "value", "list": [1, 2, 3]}
        
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "test_data.json"
            
            # 测试保存
            save_data(data, file_path)
            assert file_path.exists()
            
            # 测试加载
            loaded_data = load_data(file_path)
            assert loaded_data == data
    
    def test_save_and_load_numpy_data(self):
        """测试NumPy数据的保存和加载"""
        data = np.array([[1, 2, 3], [4, 5, 6]])
        
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "test_data.npy"
            
            # 测试保存
            save_data(data, file_path)
            assert file_path.exists()
            
            # 测试加载
            loaded_data = load_data(file_path)
            np.testing.assert_array_equal(data, loaded_data)
    
    def test_create_directories(self):
        """测试创建目录"""
        with tempfile.TemporaryDirectory() as tmpdir:
            dirs = [
                Path(tmpdir) / "dir1",
                Path(tmpdir) / "dir2" / "subdir",
                Path(tmpdir) / "dir3"
            ]
            
            create_directories(dirs)
            
            for dir_path in dirs:
                assert dir_path.exists()
                assert dir_path.is_dir() 