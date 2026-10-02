def media_notas(notas):
    return sum(notas) / len(notas)


def situacao_aluno(media):
    if media >= 7:
        return "aprovado"
    elif media >= 5:
        return "recuperacao"
    else:
        return "reprovado"
