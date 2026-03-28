// SPDX-License-Identifier: MIT
// Contracts for DePIN Supply Chain Platform

%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address

@contract_interface
namespace IDepinSupplyChain {
    func register_item(item_id: felt, location: felt, timestamp: felt) {
    }

    func update_item_status(item_id: felt, new_status: felt, location: felt, timestamp: felt) {
    }

    func get_item_details(item_id: felt) -> (location: felt, status: felt, last_updated: felt) {
    }
}

@storage_var
func item_locations(item_id: felt) -> (felt) {
}

@storage_var
func item_statuses(item_id: felt) -> (felt) {
}

@storage_var
func item_last_updated(item_id: felt) -> (felt) {
}

@constructor
func constructor() {
    return ();
}

@external
func register_item{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr: felt}(
    item_id: felt,
    location: felt,
    timestamp: felt
) {
    item_locations.write(item_id, location);
    item_statuses.write(item_id, 1); // 1 for 'Registered'
    item_last_updated.write(item_id, timestamp);
    return ();
}

@external
func update_item_status{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr: felt}(
    item_id: felt,
    new_status: felt,
    location: felt,
    timestamp: felt
) {
    // Basic authorization: only the owner or authorized entity can update
    // For simplicity, we'll skip complex auth here, but it would be added.

    item_statuses.write(item_id, new_status);
    item_locations.write(item_id, location);
    item_last_updated.write(item_id, timestamp);
    return ();
}

@view
func get_item_details{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr: felt}(
    item_id: felt
) -> (location: felt, status: felt, last_updated: felt) {
    let (location) = item_locations.read(item_id);
    let (status) = item_statuses.read(item_id);
    let (last_updated) = item_last_updated.read(item_id);
    return (location, status, last_updated);
}
