# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_timezone_to_report_schedule

Revision ID: ae1ed299413b
Revises: 030c840e3a1c
Create Date: 2021-07-09 12:18:52.057815

"""

# revision identifiers, used by Alembic.
revision = "ae1ed299413b"
down_revision = "030c840e3a1c"

import sqlalchemy as sa  # noqa: E402
from alembic import op  # noqa: E402


def upgrade():
    with op.batch_alter_table("report_schedule") as batch_op:
        batch_op.add_column(
            sa.Column(
                "timezone", sa.String(length=100), nullable=False, server_default="UTC"
            )
        )


def downgrade():
    with op.batch_alter_table("report_schedule") as batch_op:
        batch_op.drop_column("timezone")
