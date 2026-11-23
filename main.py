
from prompt_sciscreen import criar_prompt
from llm_service import analisar_resumo

print("================================")
print("  SciScreen - Triagem Cientifica")
print("================================")

objetivo = input("\nObjetivo da revisao: ").strip()

criterios = input(
    "\nCriterios de inclusao e exclusao: "
).strip()

resumo = input("\nCole o abstract: ").strip()

if not objetivo or not criterios or not resumo:
    print("\nERRO: Todos os campos sao obrigatorios.")

else:
    print("\nDados validados com sucesso!")

    prompt = criar_prompt(objetivo, criterios, resumo)

    print("\nAnalisando o abstract com GroqCloud...")
    print("Aguarde alguns instantes.\n")

    resultado = analisar_resumo(prompt)

    print("========== RESULTADO DA TRIAGEM ==========")
    print(resultado)
    print("==========================================")




