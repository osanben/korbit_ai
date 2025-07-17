# Korbit AI 项目 Makefile

.PHONY: help install install-dev test lint format clean setup all

# 默认目标
help:
	@echo "可用的命令:"
	@echo "  setup       - 完整环境设置（安装依赖和开发工具）"
	@echo "  install     - 安装项目依赖"
	@echo "  install-dev - 安装项目和开发依赖"
	@echo "  test        - 运行测试"
	@echo "  lint        - 运行代码检查"
	@echo "  format      - 格式化代码"
	@echo "  clean       - 清理临时文件"
	@echo "  all         - 运行格式化、检查和测试"

# 环境设置
setup: install-dev
	@echo "✅ 环境设置完成！"

# 安装依赖
install:
	pip install -r requirements.txt

# 安装开发依赖
install-dev:
	pip install -e ".[dev]"

# 运行测试
test:
	pytest tests/ -v --cov=src/korbit_ai --cov-report=html --cov-report=term

# 代码检查
lint:
	flake8 src/ tests/
	@echo "✅ 代码检查通过！"

# 代码格式化
format:
	black src/ tests/
	isort src/ tests/
	@echo "✅ 代码格式化完成！"

# 清理临时文件
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	@echo "✅ 清理完成！"

# 完整流程
all: format lint test
	@echo "✅ 所有检查完成！" 