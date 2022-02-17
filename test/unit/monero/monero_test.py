from test.unit.test_case import CypherpunkpayTestCase


class MoneroTest(CypherpunkpayTestCase):

    XMR_STAGENET_MAIN_ADDRESS = '5BKTP2n9Tto6fJ25fv5seHUwuyiSFk2kZJV5LKnQkXp4DknK1e28tPGiEWqbLMJ4wWamGACRW7aTZEXiqEsbgJGfK2QffLz'

    XMR_STAGENET_MAIN_ADDRESS_VIEW_PUBLIC = '419a1053fd5f7ff6841b971f66100dc9db469dd08a64a850e37e9b9d85c6a89f'
    XMR_STAGENET_MAIN_ADDRESS_VIEW_SECRET = '1543738e3ff094c144ed6697a26beb313c765ffd368b781bd4602a4c6153c305'

    XMR_STAGENET_MAIN_ADDRESS_SPEND_PUBLIC = 'fa603877c6149421d71ebe095a90aaa71538d438a7f77a6887c0cb44e6ab294c'
    XMR_STAGENET_MAIN_ADDRESS_SPEND_SECRET = '27499ed0228f443efba2a9b4307ed459cb0377d0cef77359c4e0171c4ce1a10e'

    # This belongs to us
    STEALTH_PUBLIC_1 = '53c2d7b08dc7ca09947876fb0d3e57f0863a856fa711762c08deabeb9a196464'
    # This is rest for the sender
    STEALTH_PUBLIC_2 = '0b5cd6caee5a6f9b99f2b47ada3094d80147fe8044f197d8c7f640ee4f585d58'

    def test_txo_recognized(self):
        from monero.daemon import Daemon
        from monero.wallet import Wallet
        daemon = Daemon(host='stagenet.melo.tools', port=38081)
        #tx = daemon.transactions("d65d05db90da239d4bbc2ae7ec711aa2da45c0eb62bce0078f94e90000a24362")[0]
        tx = daemon.transactions("26cb0bde5fe0ebe57806ee18d87d20ac76bf5825733b12edaa8f422e2d56bd03")[0]

        print(tx.__dict__)
        # {
        #     'hash': 'f79a10256859058b3961254a35a97a3d4d5d40e080c6275a3f9779acde73ca8d',
        #     'fee': Decimal('0.000353610000'),
        #     'height': 519608,
        #     'timestamp': datetime.datetime(2020, 2, 18, 11, 40, 36),
        #     'key': None, 'blob': None, 'confirmations': None, 'output_indices': None,
        #     'json': {
        #         'version': 2, 'unlock_time': 0, 'vin':
        #             [
        #                 {'key': {'amount': 0, 'key_offsets': [1909601, 217341, 115863, 51237, 375, 12087, 247, 243, 151, 849, 78], 'k_image': 'd9ec814b9a74da2e2df025100561c0c233f00b3d80b10f0a26f5ffd8599ada06'}}], 'vout': [{'amount': 0, 'target': {'key': 'd3eb42322566c1d48685ee0d1ad7aed2ba6210291a785ec051d8b13ae797d202'}}, {'amount': 0, 'target': {'key': '5bda44d7953e27b84022399850b59ed87408facdf00bbd1a2d4fda4bf9ebf72f'}}, {'amount': 0, 'target': {'key': '4c79c14d5d78696e72959a28a734ec192059ebabb931040b5a0714c67b507e76'}}, {'amount': 0, 'target': {'key': '64de2b358cdf96d498a9688edafcc0e25c60179e813304747524c876655a8e55'}}, {'amount': 0, 'target': {'key': '966240954892294091a48c599c6db2b028e265c67677ed113d2263a7538f9a43'}}], 'extra': [1, 146, 237, 108, 138, 102, 45, 238, 33, 161, 206, 135, 162, 175, 155, 54, 190, 224, 201, 123, 184, 53, 72, 222, 104, 30, 62, 117, 139, 247, 135, 182, 75, 4, 5, 113, 84, 189, 210, 154, 130, 14, 75, 193, 242, 17, 141, 220, 41, 99, 98, 206, 221, 184, 221, 39, 131, 165, 108, 235, 107, 103, 190, 40, 55, 174, 11, 209, 63, 23, 122, 178, 206, 172, 177, 142, 196, 198, 11, 10, 166, 58, 83, 5, 243, 98, 168, 164, 0, 135, 184, 180, 20, 151, 205, 66, 39, 23, 123, 237, 241, 232, 148, 52, 161, 122, 39, 59, 18, 163, 101, 227, 224, 141, 147, 79, 44, 212, 57, 232, 247, 109, 238, 64, 235, 146, 131, 20, 92, 231, 85, 63, 29, 33, 143, 11, 171, 126, 173, 10, 83, 32, 1, 84, 157, 86, 180, 23, 44, 186, 149, 84, 47, 112, 252, 60, 207, 29, 20, 19, 242, 150, 203, 182, 163, 148, 22, 83, 118, 207, 203, 225, 39, 157, 43, 19, 190, 161, 54, 161, 69, 224, 34, 58, 140, 154, 188, 1, 56, 29, 116, 227, 149, 18, 95], 'rct_signatures': {'type': 4, 'txnFee': 353610000, 'ecdhInfo': [{'amount': 'a3dbb31727a3e5cf'}, {'amount': 'd7a6c0054a610d15'}, {'amount': '07c8fc0b2b0fc7f6'}, {'amount': '607b8b2b1ec9f80b'}, {'amount': '4fd6e38be6204f58'}], 'outPk': ['a9f90678b5845959a1a1d14759d0b5bce3669a14bbfe74bcec241fe84650886a', 'd824808507afc632d593539f661efb418fba5ee867965662bfe6223a2c54a179', 'deae21658bb80046749f6472fc1b970950adec0bceb01d7c41cec0869d8c77ad', '1f86ab1d99a77eea46de63ef9a77cea4b40992b8838552f48fd1c7256e4fd684', '30391f552ba2a259f26041a5ac58f803a51ee862663319673f00e027cd850006']}
        #             ]
        #     },
        #     'pubkeys': [],
        #     'version': 2
        # }
        #wallet = Wallet(port=28088, user='monero', password='secret')
        outs = tx.outputs(wallet=True)
        print(outs)
        print(len(outs))
        # print(outs[0].payment.local_address)
        # print(outs[0].payment.amount)

        self.assertTrue(True)
