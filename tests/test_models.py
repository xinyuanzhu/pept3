import pytest
import torch

from tfpms import models, utils

MOCK_INPUT = {
    'sequence_integer': torch.tensor(
        [
            [
                13,
                4,
                18,
                18,
                11,
                9,
                15,
                15,
                15,
                14,
                14,
                9,
                10,
                4,
                9,
                15,
                11,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
        ]
    ),
    'collision_energy_aligned_normed': torch.tensor([[0.33]]),
    'precursor_charge_onehot': torch.tensor([[0, 0, 1, 0, 0, 0]]),
}
MOCK_INPUT['peptide_mask'] = utils.create_mask(MOCK_INPUT['sequence_integer'])


def test_prosit_structure():
    expected_output = torch.tensor(
        [
            [
                5.6023e-02,
                -1.0185e-03,
                -3.3244e-04,
                -5.6339e-05,
                -5.0099e-04,
                -4.9183e-04,
                9.6651e-02,
                -1.1973e-03,
                -7.7215e-04,
                2.9188e-01,
                -5.0194e-04,
                -3.6082e-04,
                4.3179e-02,
                -6.7944e-04,
                -3.7217e-04,
                6.1847e-02,
                -3.0873e-04,
                -2.8236e-04,
                -6.4921e-05,
                -5.0780e-04,
                -1.7689e-04,
                1.8525e-02,
                -3.3550e-04,
                -2.3973e-04,
                1.7238e-02,
                -4.6399e-04,
                -2.6510e-04,
                -9.7762e-05,
                -3.2603e-04,
                -3.2422e-04,
                2.2630e-02,
                -4.6802e-04,
                -2.9122e-04,
                -1.2624e-05,
                -2.6645e-04,
                -3.6572e-04,
                -3.6272e-05,
                -5.5409e-04,
                -3.9584e-04,
                4.2792e-02,
                -1.7437e-04,
                -5.2354e-04,
                1.7497e-02,
                -2.9365e-04,
                -2.9248e-04,
                7.3766e-03,
                -1.5967e-05,
                -5.1556e-04,
                -2.0606e-04,
                -1.7693e-04,
                -3.5843e-04,
                -1.2678e-04,
                6.2477e-02,
                -4.5684e-04,
                -5.8328e-04,
                9.3029e-03,
                -2.3070e-04,
                -3.4660e-04,
                -7.9118e-05,
                -4.1350e-04,
                -6.9945e-04,
                3.8837e-03,
                -1.9603e-04,
                -3.1830e-04,
                2.0132e-02,
                -4.0235e-04,
                -9.3022e-04,
                -9.3503e-05,
                -2.3154e-04,
                -4.2383e-04,
                -6.6261e-06,
                -4.8443e-04,
                -9.0101e-04,
                1.7171e-02,
                4.6012e-04,
                -5.1098e-04,
                1.8174e-02,
                -3.8094e-04,
                -1.0267e-03,
                2.2776e-02,
                -2.6023e-04,
                -1.1973e-03,
                1.2876e-01,
                2.9396e-03,
                -1.5280e-03,
                3.3664e-02,
                1.6610e-01,
                -2.7240e-03,
                2.4865e-01,
                1.5073e-01,
                -1.9032e-03,
                3.5875e-02,
                3.3782e-02,
                -1.8073e-03,
                2.5537e-02,
                2.4657e-01,
                -1.8446e-03,
                -1.5696e-04,
                3.0851e-02,
                -1.3719e-03,
                -1.4724e-04,
                1.0659e-01,
                -1.8716e-03,
                -3.3631e-04,
                1.3593e-03,
                -1.0641e-03,
                -4.5526e-04,
                3.4989e-02,
                -2.4141e-03,
                -3.4236e-04,
                -1.8738e-04,
                -1.4640e-03,
                -6.8656e-04,
                1.1233e-02,
                -2.6541e-03,
                -5.7517e-04,
                -6.8545e-05,
                -1.6033e-03,
                -9.0037e-04,
                -2.4769e-04,
                -2.2273e-03,
                -4.8892e-04,
                2.6444e-02,
                -1.7863e-03,
                -7.3873e-04,
                -1.9120e-04,
                -2.9776e-03,
                -8.2492e-04,
                2.8763e-02,
                -2.0114e-03,
                -1.4537e-03,
                2.2752e-02,
                -3.7736e-03,
                -9.7935e-04,
                4.6550e-02,
                -2.7701e-03,
                -9.4490e-04,
                -1.0480e-04,
                -3.6005e-03,
                -7.2444e-04,
                2.9899e-02,
                -2.4257e-03,
                -1.5452e-03,
                -3.2876e-04,
                -3.7211e-03,
                -7.2056e-04,
                -2.8388e-06,
                -2.4183e-03,
                -1.1634e-03,
                -8.9456e-04,
                -3.4940e-03,
                -9.0571e-04,
                1.1540e-02,
                -2.4473e-03,
                -1.1034e-03,
                -1.0956e-03,
                -3.4994e-03,
                -6.5191e-04,
                -2.0003e-04,
                -2.2940e-03,
                -1.1545e-03,
                -1.5345e-03,
                -3.8100e-03,
                -7.1484e-04,
                -2.2872e-04,
                -2.3434e-03,
                -1.0301e-03,
                -1.5874e-03,
                -1.6989e-03,
                -2.4112e-04,
                -3.0645e-04,
                -1.8107e-03,
                -4.1178e-04,
                -1.0868e-03,
            ]
        ]
    )
    assert 'prosit' in models.Model_Factories
    prosit = models.Model_Factories['prosit']()
    prosit.load_state_dict(
        torch.load(models.Model_Weights_Factories(
            'prosit'), map_location='cpu')
    )
    prosit = prosit.eval()
    with torch.no_grad():
        output = prosit(MOCK_INPUT).detach()
        assert (output - expected_output).abs().mean() < 1e-6


def test_pdeep_structure():
    expected_output = torch.tensor(
        [
            [
                1.4261e-01,
                1.6516e-08,
                -2.4304e-06,
                1.1251e-10,
                7.5441e-09,
                9.0658e-05,
                9.6417e-03,
                -4.2935e-10,
                -6.6895e-06,
                1.6794e-01,
                2.4583e-09,
                7.2733e-05,
                3.5120e-01,
                -1.0132e-07,
                -2.6029e-06,
                9.1689e-02,
                1.3942e-09,
                1.2850e-04,
                2.3986e-01,
                -1.3941e-05,
                2.0734e-06,
                3.5266e-02,
                4.9989e-11,
                6.7256e-05,
                3.6571e-02,
                -8.1497e-07,
                4.4557e-06,
                2.2096e-07,
                2.1205e-12,
                2.6279e-05,
                6.5595e-02,
                4.4189e-04,
                1.4407e-05,
                2.1604e-11,
                1.1584e-13,
                5.7781e-05,
                4.0818e-02,
                2.3895e-04,
                3.0181e-05,
                1.7013e-05,
                1.9012e-12,
                7.9401e-05,
                3.2077e-02,
                4.2130e-06,
                3.7363e-05,
                7.7643e-04,
                1.2091e-07,
                5.0831e-05,
                8.4644e-07,
                1.6846e-02,
                1.1409e-05,
                -5.2581e-10,
                8.0193e-02,
                7.0567e-05,
                -1.4740e-11,
                1.2358e-02,
                1.0774e-05,
                8.1202e-14,
                1.2541e-02,
                1.2221e-04,
                -2.0363e-11,
                1.1917e-06,
                6.1892e-06,
                3.5056e-13,
                1.0734e-02,
                3.0535e-05,
                -2.2770e-11,
                2.1521e-08,
                3.0614e-06,
                6.7225e-15,
                7.5966e-03,
                1.7049e-05,
                -1.8584e-11,
                1.6150e-07,
                6.1678e-06,
                5.0811e-16,
                3.2324e-03,
                4.8936e-05,
                -5.1827e-11,
                7.9820e-08,
                9.9079e-07,
                -8.3183e-10,
                4.1745e-01,
                4.9885e-05,
                -1.4565e-08,
                3.3198e-05,
                7.9081e-01,
                -6.8615e-10,
                1.6142e-01,
                1.3624e-04,
                -1.2356e-08,
                7.8897e-11,
                3.8367e-03,
                -4.1470e-10,
                9.9175e-02,
                1.0708e-03,
                -1.2004e-09,
                1.1112e-13,
                -2.9045e-06,
                -2.6657e-08,
                6.3411e-02,
                1.8717e-04,
                4.5528e-07,
                2.9588e-09,
                2.4493e-03,
                -6.7890e-07,
                1.1396e-01,
                3.2882e-04,
                2.1983e-07,
                4.7698e-11,
                2.3382e-04,
                -3.6027e-06,
                1.9831e-01,
                1.1032e-03,
                3.5466e-07,
                1.5726e-11,
                -1.5042e-06,
                -6.3954e-06,
                2.1982e-01,
                1.0363e-03,
                2.4427e-07,
                2.5157e-12,
                -6.1988e-06,
                -8.3690e-06,
                1.9373e-01,
                8.1648e-04,
                3.1634e-07,
                1.1734e-11,
                -3.9444e-06,
                -9.7818e-06,
                1.5253e-01,
                6.9309e-04,
                3.1051e-07,
                4.6203e-11,
                -1.7472e-06,
                -1.3895e-05,
                1.2444e-01,
                8.2510e-04,
                3.1489e-07,
                1.2354e-11,
                3.1796e-06,
                -2.3600e-05,
                9.1339e-02,
                1.2155e-03,
                3.3365e-07,
                8.9442e-13,
                -7.9962e-07,
                -5.5247e-05,
                7.2571e-02,
                2.8688e-03,
                2.0839e-07,
                3.4176e-14,
                -5.6299e-06,
                -1.7698e-04,
                6.2736e-02,
                1.3237e-02,
                8.7933e-08,
                2.7287e-15,
                -2.3667e-05,
                -6.9755e-04,
                5.4365e-02,
                2.7461e-02,
                1.4368e-07,
                9.0223e-16,
                -8.6822e-05,
                -8.8416e-03,
                3.9562e-02,
                2.4949e-02,
                4.6229e-07,
                2.8749e-15,
                -2.2513e-04,
                -1.1242e-02,
                2.7729e-02,
                1.6007e-02,
            ]
        ]
    )
    assert 'pdeep' in models.Model_Factories
    pdeep = models.Model_Factories['pdeep']()
    pdeep.load_state_dict(
        torch.load(models.Model_Weights_Factories('pdeep'), map_location='cpu')
    )
    pdeep = pdeep.eval()
    with torch.no_grad():
        output = pdeep(MOCK_INPUT).detach()
        assert (output - expected_output).abs().mean() < 1e-6
