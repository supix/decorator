from cacao import Cacao
from caffe import Caffe
from latte import Latte
from schiuma import Schiuma
from zucchero import Zucchero

if __name__ == "__main__":
    latte = Latte()
    latte_e_caffe = Caffe(latte)
    latte_e_caffe_dolce = Zucchero(latte_e_caffe)
    latte_e_caffe_dolce_schiumato = Schiuma(latte_e_caffe_dolce)
    latte_e_caffe_dolce_schiumato_con_cacao = Cacao(latte_e_caffe_dolce_schiumato)

    print(latte_e_caffe_dolce_schiumato_con_cacao.name())

    latte = Latte()
    latte_e_cacao = Cacao(latte)

    print(latte_e_cacao.name())