from appendix_3_model_parameters import (
    alpha,
    sigma,
    gamma_1 as g1,
    gamma_2 as g2,
    gamma_3 as g3,
    beta_1,
    beta_2,
    beta_3,
    b,
    r,
    p,
    R_0,
)


def calculate_R(
    alpha=alpha,
    sigma=sigma,
    gamma_1=g1,
    gamma_2=g2,
    gamma_3=g3,
    beta_1=beta_1,
    beta_2=beta_2,
    beta_3=beta_3,
    b=b,
    r=r,
    p=p,
    R_0=R_0,
):
    R = (
        (beta_1 / gamma_1)
        + ((1 - p) * (beta_2 / gamma_2))
        + ((1 - p) * (beta_3 / gamma_3))
        + (((p * b) / (g2 + alpha)) * (beta_2 + ((g2 * beta_3) / g3)))
        + (((p * alpha * r) / (g2 + alpha)) * ((beta_2 / g2) + (beta_3 / g3)))
    )
    return R
