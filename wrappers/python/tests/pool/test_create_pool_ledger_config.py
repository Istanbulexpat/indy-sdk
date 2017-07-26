from tests.utils import pool, storage
from indy.error import ErrorCode, IndyError

import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.mark.asyncio
async def test_create_pool_ledger_config_works(cleanup_storage):
    await pool.create_pool_ledger_config("pool_create")


@pytest.mark.asyncio
async def test_create_pool_ledger_config_works_for_empty_name(cleanup_storage):
    with pytest.raises(IndyError) as e:
        await pool.create_pool_ledger_config("")
    assert ErrorCode.CommonInvalidParam2 == e.value.error_code


@pytest.mark.asyncio
async def test_create_pool_ledger_config_works_for_config_json(cleanup_storage):
    pool_name = "pool_create"
    config = pool.create_default_pool_config(pool_name)
    await pool.create_pool_ledger_config(pool_name, None, config, None)


@pytest.mark.asyncio
async def test_create_pool_ledger_config_works_for_specific_config(cleanup_storage):
    pool_name = "pool_create"
    gen_txn_file_name = "specific_filename.txn"
    config = {
        "genesis_txn": str(storage.indy_temp_path().joinpath(gen_txn_file_name))
    }
    await pool.create_pool_ledger_config(pool_name, None, config, gen_txn_file_name)
