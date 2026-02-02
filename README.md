# 基金实时估值查询 - Vercel部署版

一个部署在 Vercel 上的基金实时估值查询工具。

## 🚀 快速部署到 Vercel

### 方法一：通过 Vercel CLI（推荐）

1. **安装 Vercel CLI**
```bash
npm install -g vercel
```

2. **登录 Vercel**
```bash
vercel login
```

3. **在项目目录下部署**
```bash
cd fund-tracker-vercel
vercel
```

4. **跟随提示完成部署**
   - 首次部署会询问项目设置
   - 选择默认配置即可
   - 部署完成后会得到一个 `.vercel.app` 域名

### 方法二：通过 Vercel 网站部署

1. **准备 GitHub 仓库**
   - 将 `fund-tracker-vercel` 文件夹内容推送到 GitHub 仓库
   
2. **导入到 Vercel**
   - 访问 [vercel.com](https://vercel.com)
   - 点击 "New Project"
   - 选择你的 GitHub 仓库
   - 点击 "Deploy"

3. **等待部署完成**
   - Vercel 会自动检测配置并部署
   - 部署成功后会获得一个访问链接

## 📁 项目结构

```
fund-tracker-vercel/
├── api/
│   └── fund.py          # Serverless Function API
├── index.html           # 前端页面
├── vercel.json          # Vercel配置文件
├── requirements.txt     # Python依赖
├── .gitignore          # Git忽略文件
└── README.md           # 说明文档
```

## ⚙️ 配置说明

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/fund.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/fund",
      "dest": "api/fund.py"
    },
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
```

这个配置文件告诉 Vercel：
- 使用 Python runtime 来运行 `api/fund.py`
- 将 `/api/fund` 请求路由到 Python function
- 其他请求直接提供静态文件

## 🔧 本地开发

1. **安装 Vercel CLI**
```bash
npm install -g vercel
```

2. **本地运行**
```bash
vercel dev
```

3. **访问**
打开浏览器访问 `http://localhost:3000`

## 📊 功能特性

- ✅ 实时查询基金估值数据
- ✅ 支持添加多个自选基金
- ✅ 自动刷新功能（每30秒）
- ✅ 数据本地保存
- ✅ 响应式设计，支持移动端
- ✅ 完全免费部署

## 🌐 API 端点

### GET /api/fund?code={基金代码}

**请求示例：**
```
GET /api/fund?code=161725
```

**响应示例：**
```json
{
  "success": true,
  "data": {
    "fundcode": "161725",
    "name": "招商中证白酒指数分级",
    "jzrq": "2024-02-01",
    "dwjz": "0.9520",
    "gsz": "0.9580",
    "gszzl": "0.63",
    "gztime": "2024-02-02 14:30"
  }
}
```

## ⚠️ 注意事项

1. **数据说明**
   - 数据来源：天天基金网
   - 估值数据仅供参考，不构成投资建议
   - 交易日 9:30-15:00 实时更新

2. **限制**
   - Vercel 免费版每月有 100GB 带宽限制
   - Serverless Function 执行时间限制 10 秒
   - 新基金可能暂无实时估值数据

3. **自定义域名**（可选）
   - 在 Vercel 项目设置中可以添加自定义域名
   - 需要在域名服务商处配置 DNS

## 🔄 更新部署

修改代码后重新部署：

```bash
vercel --prod
```

或者推送到 GitHub，Vercel 会自动重新部署。

## 🐛 故障排除

**问题：部署失败**
- 检查 `vercel.json` 格式是否正确
- 确保 Python 代码没有语法错误

**问题：API 返回 500 错误**
- 查看 Vercel 控制台的 Function Logs
- 检查基金代码是否正确

**问题：CORS 错误**
- API 已配置 CORS 允许所有来源
- 如果仍有问题，检查浏览器控制台错误信息

## 📞 技术支持

- Vercel 文档：https://vercel.com/docs
- 项目问题：检查浏览器控制台和 Vercel Function Logs

---

**免责声明**：本工具仅供个人学习和研究使用，数据来源于公开渠道，不构成任何投资建议。投资有风险，入市需谨慎。
