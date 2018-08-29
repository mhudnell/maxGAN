
import gan

## TESTING ##

data_cols = []
for frame in range(1,6):        # currently produces the wrong order
    for char in ['L', 'T', 'R', 'B']:
        for obj in range(1,6):
            data_cols.append('f' + str(frame) + char + str(obj))

# LOAD MODEL
# generator_model, discriminator_model, combined_model = getModel(data_cols, generator_model_path = 'C:\\Users\\Max\\Research\\maxGAN\\weights\\GAN_noise_4e-4__gen_weights_step_100.h5',
#                                                                      discriminator_model_path = 'C:\\Users\\Max\\Research\\maxGAN\\weights\\GAN_noise_4e-4__discrim_weights_step_100.h5')
folder_dir = 'maxGAN_bs32_lr0.0005_kd2_kg1_steps7200_DualLRexpDecay5_256node'
step = '7200'
generator_model, discriminator_model, combined_model = gan.getModel(data_cols, generator_model_path = 'C:\\Users\\Max\\Research\\maxGAN\\weights\\'+folder_dir+'\\gen_weights_step_'+step+'.h5',
                                                                     discriminator_model_path = 'C:\\Users\\Max\\Research\\maxGAN\\weights\\'+folder_dir+'\\discrim_weights_step_'+step+'.h5')

cache_prefix = folder_dir + '_step' + step
# gan.testModelMult(generator_model, discriminator_model, combined_model, cache_prefix)
gan.testModel(generator_model, discriminator_model, combined_model, cache_prefix)
# gan.testDiscrim(generator_model, discriminator_model, combined_model)