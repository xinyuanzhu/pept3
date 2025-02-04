import logging
import sys

import torch

sys.path.append('../')
from pept3 import utils
from pept3.features import generate_prosit_feature_set
from pept3.finetune import semisupervised_finetune_twofold
from pept3.models import PrositFrag, pDeep2_nomod

utils.LOGGING_LEVEL = logging.INFO

model = PrositFrag()
print('Running', model.comment())
table_file = './demo_data/demo_input.tab'

model.load_state_dict(
    torch.load('../assets/best_frag_l1_PrositFrag-1024.pth', map_location='cpu')
)
model = model.eval()

fmodel1, fmodel2, id2remove = semisupervised_finetune_twofold(model, table_file)


generate_prosit_feature_set(
    fmodel1,
    fmodel2,
    table_file,
    id2remove,
    save2='./demo_data/demo_out.tab',
    tensor_need=True,
    tensor_path='./demo_data/tensor.hdf5',
)
