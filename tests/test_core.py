"""
测试核心功能模块
"""

import pytest
import sys
from pathlib import Path

# 添加src目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from korbit_ai.core import KorbitAI


class TestKorbitAI:
    """测试 KorbitAI 类"""
    
    def test_init(self):
        """测试初始化"""
        ai = KorbitAI()
        assert ai.config == {}
        assert ai.model is None
    
    def test_init_with_config(self):
        """测试带配置的初始化"""
        config = {"model_type": "test"}
        ai = KorbitAI(config)
        assert ai.config == config
    
    def test_load_model(self):
        """测试加载模型"""
        ai = KorbitAI()
        # 这里只测试方法不抛异常
        ai.load_model("test_model_path")
    
    def test_predict(self):
        """测试预测"""
        ai = KorbitAI()
        result = ai.predict("test_input")
        assert result is None  # 目前返回 None
    
    def test_train(self):
        """测试训练"""
        ai = KorbitAI()
        # 这里只测试方法不抛异常
        ai.train("test_training_data") 