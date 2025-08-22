FROM odoo:18.0

# Switch to root user to install packages
USER root

RUN apt-get update && apt-get install -y --no-install-recommends python3-packaging \
    && rm -rf /var/lib/apt/lists/*


# Install OS packages and create directories
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-liberation \
    fonts-dejavu-core \
    fonts-noto \
    vim \
    net-tools \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/log/odoo \
    && chown -R odoo:odoo /var/log/odoo


RUN pip3 install --no-cache-dir --break-system-packages \
    "odoo-addon-component==18.*" \
    "odoo-addon-storage-backend==18.*" \
    "odoo-addon-storage-backend-s3==18.*" \
    "odoo-addon-fs-storage==18.*" \
    "odoo-addon-fs-attachment==18.*" \
    "s3fs>=2024.5.0"

# Copy initialization script
COPY init-odoo.sh /usr/local/bin/init-odoo.sh
RUN chmod +x /usr/local/bin/init-odoo.sh

# Switch back to the odoo user
USER odoo

# Set the working directory
WORKDIR /usr/lib/python3/dist-packages/odoo

# Default command
CMD ["/usr/local/bin/init-odoo.sh"]