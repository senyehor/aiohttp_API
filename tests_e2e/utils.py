from typing import Any

from repository.schemas import DeviceSchema, LocationSchema, UserSchema


def device_to_dict(
        device: DeviceSchema, owner: UserSchema, location: LocationSchema
) -> dict[str, Any]:
    return {
        'type':        device.type,
        'login':       device.login,
        'password':    device.password,
        'location_id': location.id,
        'api_user_id': owner.id
    }
