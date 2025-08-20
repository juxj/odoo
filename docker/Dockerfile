FROM odoo:18.0

# 切换到 root 用户安装字体
USER root

# 直接安装字体和必要包（使用原始官方源，最稳定）
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-liberation \
    fonts-dejavu-core \
    fonts-noto \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/log/odoo \
    && chown -R odoo:odoo /var/log/odoo

# 复制初始化脚本
COPY init-odoo.sh /usr/local/bin/init-odoo.sh
RUN chmod +x /usr/local/bin/init-odoo.sh

# 切换回 odoo 用户
USER odoo

# 设置工作目录
WORKDIR /usr/lib/python3/dist-packages/odoo

# 默认命令
# CMD ["/usr/local/bin/init-odoo.sh"]