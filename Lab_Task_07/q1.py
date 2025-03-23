from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n)
alicePubKey = alicePrivKey * curve.g

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g



aliceSharedKey = alicePrivKey * bobPubKey
bobSharedKey = bobPrivKey * alicePubKey

print("Alice public key:", compress(alicePubKey))
print("\nBob public key:", compress(bobPubKey))
print("\nAlice shared key:", compress(aliceSharedKey))
print("\nBob shared key:", compress(bobSharedKey))
